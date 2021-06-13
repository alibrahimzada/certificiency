import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Customer, CustomerCreateModel } from 'src/app/core/models/customer.model';
import { Role } from 'src/app/core/models/role.model';
import { User } from 'src/app/core/models/user.model';
import { AlertService } from 'src/app/core/services/alert.service';
import { CustomerService } from 'src/app/core/services/customer.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-upsert-customer',
  templateUrl: './upsert-customer.component.html',
  styleUrls: ['./upsert-customer.component.scss']
})
export class UpsertCustomerComponent implements OnInit {
  model = new CustomerCreateModel();
  customer = new Customer();
  role = new Role();
  user = new User();

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
    this.model.customer = this.customer;
    this.model.role = this.role;
    this.model.user = this.user;
    this.model.user.user_type = 1;
    this.model.role.role_permissions = { name: "test", key: "test" };
    if (this.model.customer.customer_id) {
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
      this.customerService.createCustomer(this.model).subscribe(response => {
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
