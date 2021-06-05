import { Component, OnInit } from '@angular/core';
import { Application } from 'src/app/core/models/application.model';
import { AlertService } from 'src/app/core/services/alert.service';
import { ApplicationService } from 'src/app/core/services/application.service';
import { CertificateService } from 'src/app/core/services/certificate.service';
import { EventService } from 'src/app/core/services/event.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-my-certificates',
  templateUrl: './my-certificates.component.html',
  styleUrls: ['./my-certificates.component.scss']
})
export class MyCertificatesComponent implements OnInit {
  certificates = [];
  events = [];
  application = new Application();

  constructor(private certificateService: CertificateService,
    private applicationService: ApplicationService,
    private eventService: EventService,
    private alertService: AlertService,
    private loadingService: LoadingService) { }

  ngOnInit(): void {
    this.getCertificates();
    this.getEvents();
  }

  getCertificates(){
    this.certificateService.getMyCertificates().subscribe(response => {
      if (response.success){
        this.certificates = response.data;
        console.log(this.certificates);
      }
      this.loadingService.setLoading(false);
    });
  }

  getEvents(){
    this.eventService.getMyEvents().subscribe(response => {
      if (response.success){
        this.events = response.data;
        console.log(this.events);
      }
      this.loadingService.setLoading(false);
    })
  }

  getApplication(id: string){
    this.applicationService.getById(id).subscribe(response => {
      if (response.success){
        this.application = response.data;
      }
      else{
        this.alertService.alert("Error!", "Event name could not fetch!", "error");
      }
    })
  }

  getEventName(id: string){
    this.getApplication(id);
    if (this.application.event_id === undefined || this.application.event_id === null) {
      return "";
    }
    let value = this.events.filter(x => x.event_id === this.application.event_id);

    if (value !== undefined && value !== null) {
      try{
        return value[0].event_name;
      }
      catch {
        return "";
      }
    }
  }

}
