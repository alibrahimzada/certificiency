import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_ENDPOINT } from '../config';
import { EventCategory } from './../models/event_category.model';

@Injectable({
  providedIn: 'root'
})
export class EventCategoryService {

  constructor(
    private httpClient: HttpClient
  ) { }

  getEventCategorys(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/event_category/all').pipe(
      map(res => res)
    )
  }

  getById(id: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/event_category/' + id).pipe(
      map(res => res)
    );
  }

  createEventCategory(event_category: EventCategory): Observable<any> {
    return this.httpClient.post(API_ENDPOINT + '/event_category/insert', event_category).pipe(
      map(res => res)
    )
  }

  updateEventCategory(event_category: EventCategory): Observable<any> {
    return this.httpClient.put(API_ENDPOINT + '/event_category/update', event_category).pipe(
      map(res => res)
    )
  }

  deleteEventCategory(id: string): Observable<any> {
    return this.httpClient.delete(API_ENDPOINT + '/event_category/delete/' + id).pipe(
      map(res => res)
    )
  }  
}