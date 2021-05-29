import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AlertService } from 'src/app/core/services/alert.service';
import { ApplicationService } from 'src/app/core/services/application.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-application',
  templateUrl: './application.component.html',
  styleUrls: ['./application.component.scss']
})
export class ApplicationComponent implements OnInit {
  applications = [];

  constructor(private applicationService: ApplicationService,
    private alertService: AlertService,
    private loadingService: LoadingService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    if (this.route.snapshot.params.id) {
      this.applicationService.getApplicationsByEventId(this.route.snapshot.params.id).subscribe(response => {
        console.log(response);
        if (response.success) {
          this.applications = response.data;
          console.log(this.applications);
        }
      })
    }
  }

}
