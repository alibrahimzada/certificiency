import { Component, OnInit } from '@angular/core';
import { Application } from 'src/app/core/models/application.model';
import { EventCategory } from 'src/app/core/models/event_category.model';
import { AlertService } from 'src/app/core/services/alert.service';
import { ApplicationService } from 'src/app/core/services/application.service';
import { EventService } from 'src/app/core/services/event.service';
import { EventCategoryService } from 'src/app/core/services/event_category.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-my-events',
  templateUrl: './my-events.component.html',
  styleUrls: ['./my-events.component.scss']
})
export class MyEventsComponent implements OnInit {
  events = [];
  eventCategories: EventCategory[];

  constructor(private eventService: EventService,
    private eventCategoryService: EventCategoryService,
    private applicationService: ApplicationService,
    private alertService: AlertService,
    private loadingService: LoadingService) { }

  ngOnInit(): void {
    this.loadingService.setLoading(true);
    this.getEvents();
    this.getEventCategories();
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

  getEventCategories(){
    this.eventCategoryService.getEventCategorys().subscribe(response => {
      if (response.success){
        this.eventCategories = response.data;
        console.log(this.eventCategories);
      }
      this.loadingService.setLoading(false);
    })
  }

  applyEvent(id: string, name: string){
    const x = confirm('Are you sure to apply for the event named ' + name + ' ?');
    if (x) {
      let application = new Application();
      application.event_id = id;
      application.applied_on = new Date();
    
      this.applicationService.createApplication(application).subscribe(response => {
        if (response.success) {
          this.getEvents();
          this.alertService.alert("Success", "Your application is submitted!", "success");
        }
      })
    }
  }

  getCategoryName(id: number){
    if (id === undefined || id === null) {
      return "";
    }
    let value = this.eventCategories.filter(x => x.event_category_id === id);

    if (value !== undefined && value !== null) {
      try{
        return value[0].event_category_name;
      }
      catch {
        return "";
      }
    }
  }

}
