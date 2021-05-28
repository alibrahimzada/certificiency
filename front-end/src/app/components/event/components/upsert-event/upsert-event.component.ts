import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Event } from 'src/app/core/models/event.model';
import { AlertService } from 'src/app/core/services/alert.service';
import { EventService } from 'src/app/core/services/event.service';
import { EventCategoryService } from 'src/app/core/services/event_category.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-upsert-event',
  templateUrl: './upsert-event.component.html',
  styleUrls: ['./upsert-event.component.scss']
})
export class UpsertEventComponent implements OnInit {
  event = new Event();
  eventCategories = [];

  constructor(private eventService: EventService,
    private eventCategoryService: EventCategoryService,
    private loadingService: LoadingService,
    private alertService: AlertService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.eventCategoryService.getEventCategorys().subscribe(response => {
      if (response.success) {
        this.eventCategories = response.data;
        console.log(response);
      }
    });
    if (this.route.snapshot.params.id) {
      this.eventService.getById(this.route.snapshot.params.id).subscribe(response => {
        if (response.success) {
          this.event = response.data;
        }
      })
    }
  }

  save() {
    if (this.event.event_id) {
      this.eventService.updateEvent(this.event).subscribe(response => {
        if (response.success) {
          this.alertService.notification('Success!', 'Event has been successfully updated!', 'success');
          this.router.navigate(['/events']);
        } else {
          this.alertService.notification('Error!', 'An error occured!', 'error');
        }
        this.loadingService.setLoading(false);
      })
    }
    else {
      this.eventService.createEvent(this.event).subscribe(response => {
        const { success } = response;
        if (success) {
          this.alertService.notification('Success!', 'Event has been successfully added!', 'success');
          this.router.navigate(['/events']);
        } else {
          this.alertService.notification('Error!', 'An error occured!', 'error');
        }
        this.loadingService.setLoading(false);
      })
    }
  }

}
