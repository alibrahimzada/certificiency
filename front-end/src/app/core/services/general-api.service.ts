import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_ENDPOINT } from './../config';

@Injectable({
  providedIn: 'root'
})
export class GeneralApiService {

  constructor(
    private httpClient: HttpClient
  ) { }

  deleteRecord(id: string, entity: 'user' | 'report' | 'license' | 'settlement'): Observable<any> {
    return this.httpClient.delete(API_ENDPOINT + '/' + entity + '/delete/' + id).pipe(
      map(res => res)
    );
  }
}
