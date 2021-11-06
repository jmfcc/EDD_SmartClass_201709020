import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router} from '@angular/router';
import { ResponseI } from 'src/app/models/generic_mdl';
import { StudentServicesService } from '../../services/student-services.service'

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  emptyInputs=false;
  studentsaved=false;
  msg:ResponseI = {};

  constructor(private loginService: StudentServicesService, private router:Router) { }

  ngOnInit(): void {
  }

  onRegis(form:NgForm):void{
    if (this.evalInput(form.value)){
      this.loginService.addStudent(form.value).subscribe(res=>{
        // this.router.navigateByUrl('/login');
        this.studentsaved=true;
        this.emptyInputs=false;
        form.reset();
        this.msg = res || "";
      });
    }else{
      this.emptyInputs=true;
      this.studentsaved=false;
    }
    // this.router.navigateByUrl('/components');
  }

  evalInput(data:any):boolean{
    if (data.carnet == '' || data.dpi == '' || data.nombre == '' || data.carrera == '' || data.correo == '' || data.password == '' || data.creditos == '' || data.edad == ''){
      return false;
    }
    return true;
  }
}
