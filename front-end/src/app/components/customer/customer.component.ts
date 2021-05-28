import { Component, OnInit } from '@angular/core';
import { AlertService } from 'src/app/core/services/alert.service';
import { CustomerService } from 'src/app/core/services/customer.service';
import { LoadingService } from 'src/app/core/services/loading.service';

@Component({
  selector: 'app-customer',
  templateUrl: './customer.component.html',
  styleUrls: ['./customer.component.scss']
})
export class CustomerComponent implements OnInit {
  customers = [];

  constructor(private customerService: CustomerService,
    private alertService: AlertService,
    private loadingService: LoadingService) { }

  ngOnInit(): void {
    this.loadingService.setLoading(true);
    this.getCustomers();
  }

  getCustomers(){
    this.customerService.getCustomers().subscribe(response => {
      if (response.success){
        this.customers = response.data;
        console.log(this.customers);
      }
      this.loadingService.setLoading(false);
    })
  }

  deleteCustomer(id: string, name: string) {
    const x = confirm('Are you sure to delete the customer named ' + name + ' ?');
    if (x) {
      this.customerService.deleteCustomer(id).subscribe(response => {
        if (response.success) {
          this.getCustomers();
        }
      })
    }
  }

}
