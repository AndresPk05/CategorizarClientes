import { Injectable } from '@angular/core';
import { Client } from './client';
@Injectable({
  providedIn: 'root'
})
export class FileCsvService {

  constructor() { }

  LoadCsv(csv:string): Client[]{
    let data = csv.split('\r\n');
    if(data.length === 0)
      return [];
    debugger;
    let resultValidation = this.ValidateCsvLoad(data[0]);
    if(!resultValidation)
      return [];

    let dataCustomers = data.map(x=> x.split(','));
    dataCustomers.shift();
    let customers : Client[] = dataCustomers.map(x => {
      let client : Client = {
        id: Number(x[0]),
        gender: x[1],
        age: Number(x[2]),
        annualIncome: Number(x[3]),
        score: Number(x[4])
      }

      return client;
    });

    return customers;
  }

  ValidateCsvLoad(row: string): boolean{
    let data = row.split(',');
    if(data.length < 4)
      return false;

    return true;
  }
}
