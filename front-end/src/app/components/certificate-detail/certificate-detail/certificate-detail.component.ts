import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AlertService } from 'src/app/core/services/alert.service';
import { CertificateService } from 'src/app/core/services/certificate.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-certificate-detail',
  templateUrl: './certificate-detail.component.html',
  styleUrls: ['./certificate-detail.component.scss']
})
export class CertificateDetailComponent implements OnInit {
  certificate: any;
  constructor(private certificateService: CertificateService,
    private alertService: AlertService,
    private loadingService: LoadingService,
    private route: ActivatedRoute) { }

  ngOnInit(): void {
    if (this.route.snapshot.params.id) {
      this.certificateService.getCertificate(this.route.snapshot.params.id).subscribe(response => {
        if (response.success) {
          this.certificate = response.data;
          console.log(this.certificate);
        }
      })
    }
  }

}
