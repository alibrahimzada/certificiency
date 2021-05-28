import { Component, OnInit } from '@angular/core';
import { AlertService } from 'src/app/core/services/alert.service';
import { EventCategoryService } from 'src/app/core/services/event_category.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-event-category',
  templateUrl: './event-category.component.html',
  styleUrls: ['./event-category.component.scss']
})
export class EventCategoryComponent implements OnInit {
  eventCategories = [];

  constructor(private eventCategoryService: EventCategoryService,
    private alertService: AlertService,
    private loadingService: LoadingService) { }

  ngOnInit(): void {
    this.loadingService.setLoading(true);
    this.getEventCategories();
  }

  getEventCategories(){
    this.eventCategoryService.getEventCategorys().subscribe(response => {
      if (response.success){
        this.eventCategories = response.data;
      }
      this.loadingService.setLoading(false);
    })
  }

  deleteEventCategory(id: string, name: string) {
    const x = confirm('Are you sure to delete the event category named ' + name + ' ?');
    if (x) {
      this.eventCategoryService.deleteEventCategory(id).subscribe(response => {
        if (response.success) {
          this.getEventCategories();
        }
      })
    }
  }
}
