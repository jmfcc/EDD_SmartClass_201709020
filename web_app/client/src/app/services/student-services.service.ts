import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
// import { AdminServicesService } from '../services/admin-services.service';

@Injectable({
  providedIn: 'root'
})
export class StudentServicesService {

  endpoint='http://localhost:3000';
  private token = '';

  constructor(private httpClient: HttpClient) { }

  addStudent(data:any){
    return this.httpClient.post(this.endpoint+'/estudiante', data);
  }
  getStudent(data:any){
    return this.httpClient.get(this.endpoint+'/estudiante', data);
  }
  getMyNotes(){
    return this.httpClient.post(this.endpoint+'/mynotes', {"carnet":this.getToken()});
  }

  logout(){
    this.token = '';
    localStorage.removeItem("ACCESS_TOKEN");
    localStorage.removeItem("EXPIRES_IN");
    localStorage.removeItem("Usuario");
  }
  
  private saveToken(token: string, expiresIn: string):void{
    localStorage.setItem("ACCESS_TOKEN", token);
    localStorage.setItem("EXPIRES_IN", expiresIn);
    this.token = token;
  }
  
  getToken(): string{
    if (this.token == ''){
      this.token = JSON.parse(localStorage.getItem("ACCESS_TOKEN") || "{}");
    }
    return this.token;
  }
  
  loggedIn(){
    return !!localStorage.getItem('ACCESS_TOKEN')
  }
}
