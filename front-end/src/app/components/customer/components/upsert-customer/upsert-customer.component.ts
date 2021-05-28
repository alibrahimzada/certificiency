import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Customer } from 'src/app/core/models/customer.model';
import { AlertService } from 'src/app/core/services/alert.service';
import { CustomerService } from 'src/app/core/services/customer.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-upsert-customer',
  templateUrl: './upsert-customer.component.html',
  styleUrls: ['./upsert-customer.component.scss']
})
export class UpsertCustomerComponent implements OnInit {
  customer = new Customer();

  constructor(private customerService: CustomerService,
    private loadingService: LoadingService,
    private alertService: AlertService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.customer.company_permissions = {};
    if (this.route.snapshot.params.id) {
      this.customerService.getById(this.route.snapshot.params.id).subscribe(response => {
        if (response.success) {
          this.customer = response.data;
        }
      })
    }
  }

  save() {
    if (this.customer.customer_id) {
      this.customerService.updateCustomer(this.customer).subscribe(response => {
        if (response.success) {
          this.alertService.notification('Success!', 'Customer has been successfully updated!', 'success');
          this.router.navigate(['/customers']);
        } else {
          this.alertService.notification('Error!', 'An error occured!', 'error');
        }
        this.loadingService.setLoading(false);
      })
    }
    else {
      this.customerService.createCustomer(this.customer).subscribe(response => {
        const { success } = response;
        if (success) {
          this.alertService.notification('Success!', 'Customer has been successfully added!', 'success');
          this.router.navigate(['/customers']);
        } else {
          this.alertService.notification('Error!', 'An error occured!', 'error');
        }
        this.loadingService.setLoading(false);
      })
    }
  }

}
