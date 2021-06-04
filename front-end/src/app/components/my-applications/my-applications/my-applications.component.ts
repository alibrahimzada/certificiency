import { Component, OnInit } from '@angular/core';
import { APPLICATION_STATUS } from 'src/app/core/models/application.model';
import { AlertService } from 'src/app/core/services/alert.service';
import { ApplicationService } from 'src/app/core/services/application.service';
import { EventService } from 'src/app/core/services/event.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-my-applications',
  templateUrl: './my-applications.component.html',
  styleUrls: ['./my-applications.component.scss']
})
export class MyApplicationsComponent implements OnInit {
  events = [];
  applications = [];
  applicationStatusTypes = APPLICATION_STATUS;
  constructor(private eventService: EventService,
    private applicationService: ApplicationService,
    private alertService: AlertService,
    private loadingService: LoadingService) { }

  ngOnInit(): void {
     this.loadingService.setLoading(true);
     this.getEvents();
     this.getApplications();
  }

  getEvents(){
    this.eventService.getMyEvents().subscribe(response => {
      if (response.success){
        this.events = response.data;
        console.log(this.events);
      }
      this.loadingService.setLoading(false);
    });
  }

  getApplications(){
    this.applicationService.getApplications().subscribe(response => {
      if (response.success){
        this.applications = response.data;
        console.log(this.applications);
      }
      this.loadingService.setLoading(false);
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

  deleteApplication(id: string, name: string){

  }

}
