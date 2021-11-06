import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ApuntesComponent } from './components/apunte/apuntes/apuntes.component';
import { NuevoApunteComponent } from './components/apunte/nuevo-apunte/nuevo-apunte.component';
import { LoginComponent } from './components/login/login.component';
import { LoginNavbarComponent } from './components/navbar/login-navbar/login-navbar.component';
import { HomeNavbarComponent } from './components/navbar/home-navbar/home-navbar.component';
import { RegisterComponent } from './components/register/register.component';
import { DashboardComponent } from './components/admin/dashboard/dashboard.component';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    ApuntesComponent,
    NuevoApunteComponent,
    LoginComponent,
    LoginNavbarComponent,
    HomeNavbarComponent,
    RegisterComponent,
    DashboardComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
