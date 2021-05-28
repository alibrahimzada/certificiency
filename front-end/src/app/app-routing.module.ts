import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UpsertCustomerComponent } from './components/customer/components/upsert-customer/upsert-customer.component';
import { CustomerComponent } from './components/customer/customer.component';
import { UpsertEventCategoryComponent } from './components/event-category/components/upsert-event-category/upsert-event-category.component';
import { EventCategoryComponent } from './components/event-category/event-category.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
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
      }
    ]
  },
  {
    path: 'login',
    component: LoginComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
