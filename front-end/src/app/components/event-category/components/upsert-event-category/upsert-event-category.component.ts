import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { EventCategory } from 'src/app/core/models/event_category.model';
import { AlertService } from 'src/app/core/services/alert.service';
import { EventCategoryService } from 'src/app/core/services/event_category.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-upsert-event-category',
  templateUrl: './upsert-event-category.component.html',
  styleUrls: ['./upsert-event-category.component.scss']
})
export class UpsertEventCategoryComponent implements OnInit {
  eventCategory = new EventCategory();

  constructor(private eventCategoryService: EventCategoryService,
    private loadingService: LoadingService,
    private alertService: AlertService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    if (this.route.snapshot.params.id) {
      this.eventCategoryService.getById(this.route.snapshot.params.id).subscribe(response => {
        if (response.success) {
          this.eventCategory = response.data;
        }
      })
    }
  }

  save() {
    if (this.eventCategory.event_category_id) {
      this.eventCategoryService.updateEventCategory(this.eventCategory).subscribe(response => {
        if (response.success) {
          this.alertService.notification('Success!', 'Event category has been successfully updated!', 'success');
          this.router.navigate(['/event-categories']);
        } else {
          this.alertService.notification('Error!', 'An error occured!', 'error');
        }
        this.loadingService.setLoading(false);
      })
    }
    else {
      this.eventCategoryService.createEventCategory(this.eventCategory).subscribe(response => {
        const { success } = response;
        if (success) {
          this.alertService.notification('Success!', 'Event category has been successfully added!', 'success');
          this.router.navigate(['/event-categories']);
        } else {
          this.alertService.notification('Error!', 'An error occured!', 'error');
        }
        this.loadingService.setLoading(false);
      })
    }
  }
}
