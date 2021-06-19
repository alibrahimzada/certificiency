import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { APPLICATION_STATUS } from 'src/app/core/models/application.model';
import { Certificate } from 'src/app/core/models/certificate.model';
import { AlertService } from 'src/app/core/services/alert.service';
import { ApplicationService } from 'src/app/core/services/application.service';
import { CertificateService } from 'src/app/core/services/certificate.service';
import { EventService } from 'src/app/core/services/event.service';
import { LoadingService } from 'src/app/core/services/loading.service';
import { UserService } from 'src/app/core/services/user.service';

declare const $: any;
@Component({
  selector: 'app-application',
  templateUrl: './application.component.html',
  styleUrls: ['./application.component.scss']
})
export class ApplicationComponent implements OnInit {
  applications = [];
  users = [];
  events = [];
  applicationStatusTypes = APPLICATION_STATUS;
  newStatusBody = {
    id: '',
    status: 0
  };

  constructor(private applicationService: ApplicationService,
    private alertService: AlertService,
    private loadingService: LoadingService,
    private userService: UserService,
    private eventService: EventService,
    private certificateService: CertificateService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    if (this.route.snapshot.params.id) {
      console.log("Applications 1");
      this.applicationService.getApplicationsByEventId(this.route.snapshot.params.id).subscribe(response => {
        // if (response.success) {
          this.applications = response.data;
          console.log("Applications");
          console.log(response);
        // }
      })
    }

    this.getUsers();
    this.getEvents();
  }

  getUsers(){
    this.userService.getUsers().subscribe(response => {
      if (response.success){
        this.users = response.data;
        // console.log(this.users);
      }
      else {
        this.alertService.notification("Error!", "Users could not fetch!", "error");
      }
    });
  }

  getEvents(){
    this.eventService.getEvents().subscribe(response => {
      if (response.success){
        this.events = response.data;
        console.log(this.events);
      }
      else {
        this.alertService.notification("Error!", "Events could not fetch!", "error");
      }
    });
  }

  getEventName(id: string){
    if (id === undefined || id === null) {
      return "";
    }
    let value = this.events.filter(x => x.event_id === id);

    if (value !== undefined && value !== null) {
      try{
        return value[0].event_name;
      }
      catch {
        return "";
      }
    }
  }

  getEventLocation(id: string){
    if (id === undefined || id === null) {
      return "";
    }
    let value = this.events.filter(x => x.event_id === id);

    if (value !== undefined && value !== null) {
      try{
        return value[0].event_location;
      }
      catch {
        return "";
      }
    }
  }

  getEventStartDate(id: string){
    if (id === undefined || id === null) {
      return "";
    }
    let value = this.events.filter(x => x.event_id === id);

    if (value !== undefined && value !== null) {
      try{
        return value[0].event_start_date;
      }
      catch {
        return "";
      }
    }
  }

  getEventEndDate(id: string){
    if (id === undefined || id === null) {
      return "";
    }
    let value = this.events.filter(x => x.event_id === id);

    if (value !== undefined && value !== null) {
      try{
        return value[0].event_end_date;
      }
      catch {
        return "";
      }
    }
  }

  getApplicationStatus(status: number) {
    if (status === undefined || status === null) {
      return "";
    }
    let value = this.applicationStatusTypes.filter(x => x.code === status);

    if (value !== undefined && value !== null) {
      try{
        return value[0].text;
      }
      catch {
        return "";
      }
    }
  }

  getUserFirstName(id: string){
    
    if (id === undefined || id === null) {
      return "";
    }
    let value = this.users.filter(x => x.user_id === id);
    
    if (value !== undefined && value !== null) {
      try{
        return value[0].first_name;
      }
      catch {
        return "";
      }
    }
  }

  getUserLastName(id: string){
    if (id === undefined || id === null) {
      return "";
    }
    let value = this.users.filter(x => x.user_id === id);

    if (value !== undefined && value !== null) {
      try{
        return value[0].last_name;
      }
      catch {
        return "";
      }
    }
  }

  getUserEmail(id: string){
    if (id === undefined || id === null) {
      return "";
    }
    let value = this.users.filter(x => x.user_id === id);

    if (value !== undefined && value !== null) {
      try{
        return value[0].email;
      }
      catch {
        return "";
      }
    }
  }

  showUpdateStatusModal(application: any){
    this.newStatusBody = {
      id: application.application_id,
      status: application.application_status
    }
    $('#updateStatus').modal('show')
  }
  hideUpdateStatusModal() {
    $('#updateStatus').modal('hide');
    this.newStatusBody = {
      id: '',
      status: 0
    }
  }

  updateStatus() {
    this.applicationService.updateStatus(this.newStatusBody.id, this.newStatusBody.status).subscribe(response => {
      if (response.success) {
        this.alertService.notification('Success!', 'Applicatin status updated!', 'success');
        if (this.route.snapshot.params.id) {
          this.applicationService.getApplicationsByEventId(this.route.snapshot.params.id).subscribe(response => {
            if (response.success) {
              this.applications = response.data;
              console.log(this.applications);
            }
          })
        }
    
        this.getUsers();
        this.getEvents();
        this.hideUpdateStatusModal();
      } else {
        this.alertService.notification('Error!', 'Status could not updated', 'error');
      }
    })
  }

  createCertificate(){
    let certificate = new Certificate();
    certificate.application_id = this.newStatusBody.id;
    certificate.certificate_link = "";
    certificate.certified_on = new Date();
    certificate.is_public = true;
    this.certificateService.createCertificate(certificate).subscribe(response => {
      if (response.success){
        this.alertService.alert("Success!", "Certificate created!", "success");
        this.newStatusBody.status = 7;
        this.updateStatus();
      } else {
        this.alertService.alert("Error!", "Certificate could not create!", "error");
      }
    })
  }

}
