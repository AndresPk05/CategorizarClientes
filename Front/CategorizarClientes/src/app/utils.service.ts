import { Injectable } from '@angular/core';
import { Row } from './row';
import { GroupCliente } from './groupClient';

@Injectable({
  providedIn: 'root'
})


export class UtilsService {

  constructor() { }

  groupRowByLabel(rows: Row[]): GroupCliente{
    const result = rows.reduce((group: GroupCliente, item) => {
      if (!group[item.label.toString()]) {
       group[item.label.toString()] = [];
      }

      group[item.label.toString()].push(item);
      return group;
     }, {});

     return result;
  }

  getLabels(rows: Row[]): Number[]{
    let labels: Number[] = [];
    rows.forEach((item: Row) => {
      if(!labels.includes(item.label))
        labels.push(item.label);
    });
    return labels;
  }
}
