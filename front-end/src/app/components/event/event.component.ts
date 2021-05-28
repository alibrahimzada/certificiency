import { Component, OnInit } from '@angular/core';
import { EventCategory } from 'src/app/core/models/event_category.model';
import { AlertService } from 'src/app/core/services/alert.service';
import { EventService } from 'src/app/core/services/event.service';
import { EventCategoryService } from 'src/app/core/services/event_category.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-event',
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.scss']
})
export class EventComponent implements OnInit {
  events = [];
  eventCategories: EventCategory[];

  constructor(private eventService: EventService,
    private eventCategoryService: EventCategoryService,
    private alertService: AlertService,
    private loadingService: LoadingService) { }

  ngOnInit(): void {
    this.loadingService.setLoading(true);
    this.getEvents();
    this.getEventCategories();
  }

  getEvents(){
    this.eventService.getEvents().subscribe(response => {
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

  deleteEvent(id: string, name: string) {
    const x = confirm('Are you sure to delete the event named ' + name + ' ?');
    if (x) {
      this.eventService.deleteEvent(id).subscribe(response => {
        if (response.success) {
          this.getEvents();
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
