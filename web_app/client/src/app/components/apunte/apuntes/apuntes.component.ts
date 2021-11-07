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
    //   console.log(typeof(this.msg.response));
    //   console.log(JSON.parse(this.msg.response || ""))
    //   if (this.msg.response instanceof Array){
    //     console.log("si es array")
    //   }
    });
  }

  deleteN(pos:any): void {

  }

}
