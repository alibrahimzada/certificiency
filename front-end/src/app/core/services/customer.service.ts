import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_ENDPOINT } from '../config';
import { Customer } from './../models/customer.model';

@Injectable({
  providedIn: 'root'
})
export class CustomerService {

  constructor(
    private httpClient: HttpClient
  ) { }

  getCustomers(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/customer/all').pipe(
      map(res => res)
    )
  }

  getById(id: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/customer/' + id).pipe(
      map(res => res)
    );
  }

  getStats(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/report/customer-stats').pipe(
      map(res => res)
    );
  }

  createCustomer(customer: Customer): Observable<any> {
    return this.httpClient.post(API_ENDPOINT + '/customer/insert', customer).pipe(
      map(res => res)
    )
  }

  updateCustomer(customer: Customer): Observable<any> {
    return this.httpClient.put(API_ENDPOINT + '/customer/update', customer).pipe(
      map(res => res)
    )
  }

  deleteCustomer(id: string): Observable<any> {
    return this.httpClient.delete(API_ENDPOINT + '/customer/delete/' + id).pipe(
      map(res => res)
    )
  }

  
}
