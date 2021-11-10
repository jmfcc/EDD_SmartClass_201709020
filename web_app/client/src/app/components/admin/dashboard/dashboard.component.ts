import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { Router } from '@angular/router';
import { ResponseI } from 'src/app/models/generic_mdl';
import { AdminServicesService } from 'src/app/services/admin-services.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  msg:ResponseI = {};
  report:ResponseI = {};
  safeHtml: SafeHtml = "";

  constructor(private adminService:AdminServicesService, private router:Router, private sanitizer: DomSanitizer) { }

  ngOnInit(): void {
  }

  loadStudent(form:any): void {
    // console.log(form.value)
    if (form.value.path != ""){
      this.adminService.load_S(form.value).subscribe(res=>{
        this.msg = res || "";
        form.reset();
      });
    }else{
      this.msg.response = "El campo de la direccion del archivo de estudiantes está vacía"
    }
  }
  loadNotes(form:any): void {
    // console.log(form.value)
    if (form.value.path != ""){
      this.adminService.load_N(form.value).subscribe(res=>{
        this.msg = res || "";
        form.reset();
      });
    }else{
      this.msg.response = "El campo de la direccion del archivo de apuntes está vacía"
    }
  }
  loadCourses(form:any): void {
    // console.log(form.value)
    if (form.value.path != ""){
      this.adminService.load_C(form.value).subscribe(res=>{
        this.msg = res || "";
        form.reset();
      });
    }else{
      this.msg.response = "El campo de la direccion del archivo de cursos está vacía"
    }
  }

  generate(): void {
    this.adminService.gen_key().subscribe(res=>{
      this.msg = res || "";
    });
  }

  reportThash(): void {
    this.adminService.reportTHash().subscribe(res=>{
      this.report = res || "";
      this.generateComponents()
    });
  }
  reportPensum(): void {
    this.adminService.reportPens().subscribe(res=>{
      this.report = res || "";
      this.generateComponents()
    });
  }
  
  reportStud(val:any): void {
    console.log(val);
    var d = {"tipo":0, "enc":true};
    if (val == 0){
      d = {"tipo":0, "enc":false};
    }
    this.adminService.reportStud(d).subscribe(res=>{
      this.report = res || "";
      this.generateComponents()
    });
  }

  generateComponents(): void{
    this.safeHtml = this.sanitizer.bypassSecurityTrustHtml(this.report.response || "")
  }
}
