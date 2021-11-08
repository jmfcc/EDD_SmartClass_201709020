import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { JwtResponseI } from '../models/jwt-response';
import { UserI } from '../models/login-mdl';
import { ResponseI } from '../models/generic_mdl';
import { JsonPipe } from '@angular/common';
import { ReportI } from '../models/mdl_rep';

@Injectable({
  providedIn: 'root'
})
export class AdminServicesService {

  endpoint='http://localhost:3000';
  private token = '';


  constructor(private httpClient: HttpClient) { }

  gen_key(){
    return this.httpClient.get(this.endpoint+'/genkey');
  }
  reportTHash(){
    return this.httpClient.get(this.endpoint+'/reporthash');
  }
  reportStud(data:any){
    return this.httpClient.post(this.endpoint+'/reporte', data);
  }
  reportPens(data:any){
    return this.httpClient.post(this.endpoint+'/reporte', data);
  }
  // reportNotes(data:any){
  //   return this.httpClient.post(this.endpoint+'/reporte', data);
  // }

  login(data:UserI): Observable<JwtResponseI>{
    return this.httpClient.post<JwtResponseI>(this.endpoint+'/login',
    data).pipe(tap(
      (res: JwtResponseI) => {
        if (res.accesTkn != '') {
            this.saveToken(res.accesTkn || "", res.expiresIn || "");
          }
        }
      ));
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
