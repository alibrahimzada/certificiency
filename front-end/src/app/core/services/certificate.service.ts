import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_ENDPOINT } from '../config';
import { Certificate } from './../models/certificate.model';

@Injectable({
  providedIn: 'root'
})
export class CertificateService {

  constructor(
    private httpClient: HttpClient
  ) { }

  getCertificates(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/certificate/all').pipe(
      map(res => res)
    )
  }

  getMyCertificates(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/certificate/my-certificates').pipe(
      map(res => res)
    )
  }
  // /api/v1/certificate/<certificate_id>/validate-certificate
  getById(id: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/certificate/' + id).pipe(
      map(res => res)
    );
  }

  getCertificate(id: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/certificate/' + id + '/validate-certificate').pipe(
      map(res => res)
    );
  }

  createCertificate(certificate: Certificate): Observable<any> {
    return this.httpClient.post(API_ENDPOINT + '/certificate/insert', certificate).pipe(
      map(res => res)
    )
  }

  updateCertificate(certificate: Certificate): Observable<any> {
    return this.httpClient.put(API_ENDPOINT + '/certificate/', certificate).pipe(
      map(res => res)
    )
  }

  deleteCertificate(id: string): Observable<any> {
    return this.httpClient.delete(API_ENDPOINT + '/certificate/' + id).pipe(
      map(res => res)
    )
  }  
}
