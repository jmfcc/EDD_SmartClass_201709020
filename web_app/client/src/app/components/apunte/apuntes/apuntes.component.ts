import { Component, OnInit } from '@angular/core';
import { ResponseI } from 'src/app/models/generic_mdl';
import { NotesI } from 'src/app/models/mdl_notes';
import { StudentServicesService } from 'src/app/services/student-services.service';

@Component({
  selector: 'app-apuntes',
  templateUrl: './apuntes.component.html',
  styleUrls: ['./apuntes.component.css']
})
export class ApuntesComponent implements OnInit {

  msg:ResponseI = {};
  dataN:any = {};

  constructor(private studentService:StudentServicesService) { }

  ngOnInit(): void {
    this.getNotes()
  }

  getNotes(): void {
    this.studentService.getMyNotes().subscribe(res=>{
      this.dataN = res || "";
      console.log(this.dataN);
      if (!Array.isArray(this.dataN.response)){
        this.msg = res || "";
      }
    });
  }

  deleteN(pos:any): void {

  }

}
