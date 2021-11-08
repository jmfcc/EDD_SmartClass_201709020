import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ResponseI } from 'src/app/models/generic_mdl';
import { NotesI } from 'src/app/models/mdl_notes';
import { StudentServicesService } from 'src/app/services/student-services.service';

@Component({
  selector: 'app-nuevo-apunte',
  templateUrl: './nuevo-apunte.component.html',
  styleUrls: ['./nuevo-apunte.component.css']
})
export class NuevoApunteComponent implements OnInit {

  msg:ResponseI = {};
  note:NotesI = {};

  constructor(private studentService:StudentServicesService, private router:Router) { }

  ngOnInit(): void {
  }

  saveNote(form:any): void {
    console.log(form.value);
    this.note = form.value;
    this.studentService.saveMyNote(this.note).subscribe(res=>{
      form.reset();
      this.msg = res;
    });

  }
}
