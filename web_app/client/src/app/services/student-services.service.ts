import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NotesI } from '../models/mdl_notes';
// import { AdminServicesService } from '../services/admin-services.service';

@Injectable({
  providedIn: 'root'
})
export class StudentServicesService {

  endpoint = 'http://localhost:3000';
  private token = '';

  constructor(private httpClient: HttpClient) { }

  addStudent(data: any) {
    return this.httpClient.post(this.endpoint + '/estudiante', data);
  }
  getStudent(data: any) {
    return this.httpClient.get(this.endpoint + '/estudiante', data);
  }
  getMyNotes() {
    return this.httpClient.post(this.endpoint + '/mynotes', { "carnet": this.getToken() });
  }
  saveMyNote(data: NotesI) {
    return this.httpClient.post(this.endpoint + '/notes',
      {
        "carnet": this.getToken(),
        "Titulo": data.titulo,
        "Contenido": data.contenido
      });
  }
  getCoursePrerequisites(data: any) {
    return this.httpClient.post(this.endpoint + '/reporte',
      {
        "tipo": 5,
        "codigo": data.codigo 
      });
  }
  getMyCourses(data: any) {
    return this.httpClient.post(this.endpoint + '/reporte',
      {
        "tipo": 5,
        "codigo": data.codigo 
      });
  }
  assignCourse(data: any) {
    return this.httpClient.post(this.endpoint + '/reporte', data);
  }

  logout() {
    this.token = '';
    localStorage.removeItem("ACCESS_TOKEN");
    localStorage.removeItem("EXPIRES_IN");
    localStorage.removeItem("Usuario");
  }

  private saveToken(token: string, expiresIn: string): void {
    localStorage.setItem("ACCESS_TOKEN", token);
    localStorage.setItem("EXPIRES_IN", expiresIn);
    this.token = token;
  }

  getToken(): string {
    if (this.token == '') {
      this.token = JSON.parse(localStorage.getItem("ACCESS_TOKEN") || "{}");
    }
    return this.token;
  }

  loggedIn() {
    return !!localStorage.getItem('ACCESS_TOKEN')
  }
}
