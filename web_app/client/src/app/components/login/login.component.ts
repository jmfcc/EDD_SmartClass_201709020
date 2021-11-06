import { JsonpInterceptor } from '@angular/common/http';
import { Component, NgModule, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { ResponseI } from 'src/app/models/generic_mdl';
import { JwtResponseI } from 'src/app/models/jwt-response';
import { AdminServicesService } from '../../services/admin-services.service'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  msg:string = "";

  constructor(private authService:AdminServicesService, private router:Router) { }

  ngOnInit(): void {
    this.authService.logout()
  }

  onLogin(form:any): void {
    if (this.evalInput(form.value)){
      console.log('Login', form.value.carnet);
      this.authService.login(form.value).subscribe(res =>{
        console.log(res.valueOf());
        if (res.rol == "admin"){
          this.router.navigate(['/admindashboard']);
        }else if (res.rol == "student"){
          this.router.navigate(['/nuevoapunte']);
        }else{
          this.msg = "Error: Verifica tus datos";
        }
      });
    } else {
      this.msg = "Error: Debe llenar todos los campos"
    }
   }

   evalInput(data:any):boolean{
    if (data.carnet == '' || data.password == ''){
      return false;
    }
    return true;
  }
}
