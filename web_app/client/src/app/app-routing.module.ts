import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {LoginComponent} from './components/login/login.component';
import {RegisterComponent} from './components/register/register.component';
import {ApuntesComponent} from './components/apunte/apuntes/apuntes.component';
import {NuevoApunteComponent} from './components/apunte/nuevo-apunte/nuevo-apunte.component';
import {CursosComponent} from './components/cursos/cursos.component';
import {DashboardComponent} from './components/admin/dashboard/dashboard.component';

const routes: Routes = [
    {
      path: '',
      redirectTo: '/login',
      pathMatch: 'full',
  },
  {
      path: 'login',
      component: LoginComponent
  },
  {
      path: 'register',
      component: RegisterComponent
  },
  {
    path: 'apuntes',
    component: ApuntesComponent
  },
  {
    path: 'nuevoapunte',
    component: NuevoApunteComponent
  },
  {
    path: 'admindashboard',
    component: DashboardComponent
  },
  {
    path: 'cursos',
    component: CursosComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
