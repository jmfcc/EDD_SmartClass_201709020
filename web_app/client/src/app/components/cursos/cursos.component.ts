import { Component, OnInit } from '@angular/core';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { ResponseI } from 'src/app/models/generic_mdl';
import { StudentServicesService } from 'src/app/services/student-services.service';

@Component({
  selector: 'app-cursos',
  templateUrl: './cursos.component.html',
  styleUrls: ['./cursos.component.css']
})
export class CursosComponent implements OnInit {

  msg:ResponseI = {};
  msg2:ResponseI = {};
  report:ResponseI = {};
  safeHtml: SafeHtml = "";
  safeHtmlMyCourses: SafeHtml = "";

  constructor(private studentService:StudentServicesService, private sanitizer: DomSanitizer) { }

  ngOnInit(): void {
  }

  redCurso(form:any): void {
    console.log(form.value)
    if (form.value.codigo != ""){
      this.studentService.getCoursePrerequisites(form.value).subscribe(res=>{
        this.report = res || "";
        this.msg.response = "";
        this.generateComponents()
      });
    }else{
      this.msg.response = "Debes esciribir un codigo de curso"
    }
  }
  asingCurso(form:any): void {
    console.log(form.value)
    if (form.value.codigo != ""){
      this.studentService.assignCourse(form.value).subscribe(res=>{
        this.report = res || "";
        this.msg2.response = "";
        this.generateComponents()
      });
    }else{
      this.msg2.response = "Debes esciribir un codigo de curso"
    }
  }

  generateComponents(): void{
    this.safeHtml = this.sanitizer.bypassSecurityTrustHtml(this.report.response || "")
  }
  generateComponentsC(): void{
    this.safeHtmlMyCourses = this.sanitizer.bypassSecurityTrustHtml(this.report.response || "")
  }

}
