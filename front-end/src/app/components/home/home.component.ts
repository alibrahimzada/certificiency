import { Component, OnInit } from '@angular/core';
import { CustomerService } from 'src/app/core/services/customer.service';
import { LoadingService } from 'src/app/core/services/loading.service';
import { RoleService } from './../../core/services/role.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  stats: any;

  constructor(
    public roleService: RoleService,
    public customerService: CustomerService,
    public loadingService: LoadingService
  ) { }

  ngOnInit(): void {
    this.loadingService.setLoading(true);
    this.getStats();
  }

  getStats(){
    this.customerService.getStats().subscribe(response => {
      if (response.success){
        this.stats = response.data;
        console.log(this.stats);
      }
      this.loadingService.setLoading(false);
    })
  }

}
