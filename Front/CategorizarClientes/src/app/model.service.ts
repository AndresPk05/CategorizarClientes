import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Client } from './client';

@Injectable({
  providedIn: 'root'
})
export class ModelService {
  rutaApi = "http://127.0.0.1:8000";
  constructor(private http: HttpClient) {}

  getModelo(clients: Client[]): any{
    try {
      let result = this.http.post(this.rutaApi + "/train", clients);
      return result;
    } catch (error) {
      console.log(error);
    }
  }
}
