import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgSelectModule } from '@ng-select/ng-select';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { NgxFileDropModule } from 'ngx-file-drop';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { UpsertUserComponent } from './components/users/components/upsert-user/upsert-user.component';
import { UsersComponent } from './components/users/users.component';
import { IsVisibleForUserDirective } from './core/directives/is-visible-for-user.directive';
import { GeneralInterceptor } from './core/interceptors/general.interceptor';
import { AlertService } from './core/services/alert.service';
import { AuthService } from './core/services/auth.service';
import { MainLayoutComponent } from './layouts/main-layout/main-layout.component';
import { RolesComponent } from './components/roles/roles.component';
import { UpsertRoleComponent } from './components/roles/components/upsert-role/upsert-role.component';
import { CustomerComponent } from './components/customer/customer.component';
import { EventCategoryComponent } from './components/event-category/event-category.component';
import { EventComponent } from './components/event/event.component';
import { ApplicationComponent } from './components/application/application.component';
import { CertificateComponent } from './components/certificate/certificate.component';
import { UpsertEventCategoryComponent } from './components/event-category/components/upsert-event-category/upsert-event-category.component';
import { UpsertCustomerComponent } from './components/customer/components/upsert-customer/upsert-customer.component';
import { UpsertEventComponent } from './components/event/components/upsert-event/upsert-event.component';
import { CertificateDetailComponent } from './components/certificate-detail/certificate-detail/certificate-detail.component';
import { MyEventsComponent } from './components/my-events/my-events/my-events.component';
import { ProfileComponent } from './components/profile/profile/profile.component';
import { MyApplicationsComponent } from './components/my-applications/my-applications/my-applications.component';
import { MyCertificatesComponent } from './components/my-certificates/my-certificates/my-certificates.component';
@NgModule({
  declarations: [
    AppComponent,
    UsersComponent,
    MainLayoutComponent,
    LoginComponent,
    UpsertUserComponent,
    IsVisibleForUserDirective,
    HomeComponent,
    RolesComponent,
    UpsertRoleComponent,
    CustomerComponent,
    EventCategoryComponent,
    EventComponent,
    ApplicationComponent,
    CertificateComponent,
    UpsertEventCategoryComponent,
    UpsertCustomerComponent,
    UpsertEventComponent,
    CertificateDetailComponent,
    MyEventsComponent,
    ProfileComponent,
    MyApplicationsComponent,
    MyCertificatesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgSelectModule,
    FormsModule,
    HttpClientModule,
    NgxFileDropModule,
    NgxChartsModule,
    BrowserAnimationsModule,
  ],
  providers: [{
    provide: HTTP_INTERCEPTORS,
    useClass: GeneralInterceptor,
    multi: true
  }, AuthService, AlertService],
  bootstrap: [AppComponent]
})
export class AppModule { }
