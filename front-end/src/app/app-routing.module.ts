import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ApplicationComponent } from './components/application/application.component';
import { CertificateDetailComponent } from './components/certificate-detail/certificate-detail/certificate-detail.component';
import { UpsertCustomerComponent } from './components/customer/components/upsert-customer/upsert-customer.component';
import { CustomerComponent } from './components/customer/customer.component';
import { UpsertEventCategoryComponent } from './components/event-category/components/upsert-event-category/upsert-event-category.component';
import { EventCategoryComponent } from './components/event-category/event-category.component';
import { UpsertEventComponent } from './components/event/components/upsert-event/upsert-event.component';
import { EventComponent } from './components/event/event.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { MyApplicationsComponent } from './components/my-applications/my-applications/my-applications.component';
import { MyCertificatesComponent } from './components/my-certificates/my-certificates/my-certificates.component';
import { MyEventsComponent } from './components/my-events/my-events/my-events.component';
import { ProfileComponent } from './components/profile/profile/profile.component';
import { UpsertRoleComponent } from './components/roles/components/upsert-role/upsert-role.component';
import { RolesComponent } from './components/roles/roles.component';
import { UpsertUserComponent } from './components/users/components/upsert-user/upsert-user.component';
import { UsersComponent } from './components/users/users.component';
import { AuthGuard } from './core/guards/auth.guard';
import { MainLayoutComponent } from './layouts/main-layout/main-layout.component';


const routes: Routes = [
  {
    path: '',
    component: MainLayoutComponent,
    children: [
      {
        path: '',
        component: HomeComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'users',
        component: UsersComponent,
        //canActivate: [AuthGuard]
      },
      {
        path: 'users/new',
        component: UpsertUserComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'users/detail/:id',
        component: UpsertUserComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'roles',
        component: RolesComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'roles/new',
        component: UpsertRoleComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'roles/detail/:id',
        component: UpsertRoleComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'event-categories',
        component: EventCategoryComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'event-categories/new',
        component: UpsertEventCategoryComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'event-categories/detail/:id',
        component: UpsertEventCategoryComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'events',
        component: EventComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'events/new',
        component: UpsertEventComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'events/detail/:id',
        component: UpsertEventComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'my-events',
        component: MyEventsComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'my-applications',
        component: MyApplicationsComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'my-certificates',
        component: MyCertificatesComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'customers',
        component: CustomerComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'customers/new',
        component: UpsertCustomerComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'customers/detail/:id',
        component: UpsertCustomerComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'applications/:id',
        component: ApplicationComponent,
        canActivate: [AuthGuard]
      },
      {
        path: 'profile',
        component: ProfileComponent,
        canActivate: [AuthGuard]
      }
    ]
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'certificate-detail/:id',
    component: CertificateDetailComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
