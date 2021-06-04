import { Component, OnInit } from '@angular/core';
import { AlertService } from 'src/app/core/services/alert.service';
import { ApplicationService } from 'src/app/core/services/application.service';
import { CertificateService } from 'src/app/core/services/certificate.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-my-certificates',
  templateUrl: './my-certificates.component.html',
  styleUrls: ['./my-certificates.component.scss']
})
export class MyCertificatesComponent implements OnInit {
  certificates = [];
  constructor(private certificateService: CertificateService,
    private applicationService: ApplicationService,
    private alertService: AlertService,
    private loadingService: LoadingService) { }

  ngOnInit(): void {
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

}
