import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FileCsvService } from '../file-csv.service';
import { Client } from '../client';
import { GridClientsComponent } from '../grid-clients/grid-clients.component';
import { ModelService } from '../model.service';
import { UtilsService } from '../utils.service';
import { GroupCliente } from '../groupClient';
import { Row } from '../row';
import { GraficComponent } from '../grafic/grafic.component';

@Component({
  selector: 'app-clients-upload',
  standalone: true,
  imports: [CommonModule, GridClientsComponent, GraficComponent],
  templateUrl: './clients-upload.component.html',
  styleUrl: './clients-upload.component.css'
})
export class ClientsUploadComponent {
  fileService : FileCsvService = inject(FileCsvService);
  clients: Client[] = [];
  modelService = inject(ModelService);
  utils = inject(UtilsService);
  dataGrouped : GroupCliente = {} as GroupCliente;
  labels: Number[] = [];

  LoadFile(event: Event): void{
    let resultValidation = this.ValidateFile(event);
    if(!resultValidation)
      return;

    const target = event.target as HTMLInputElement;
    const files = target.files as FileList;
    const file = files[0];
    const reader = new FileReader();

    reader.readAsText(file);
    reader.onload = () => {
      const csv = reader.result as string;
      this.clients = this.fileService.LoadCsv(csv);
    }
  }

  ValidateFile(event: Event): boolean{
    const target = event.target as HTMLInputElement;
    const files = target.files as FileList;
    if(files.length === 0)
      return false;
    const file = files[0];
    if(file.type !== 'text/csv')
      return false;
    return true;
  }

  SaveClients(): void{
    this.modelService
    .getModelo(this.clients)
    .subscribe((data: string) => {
      let rowsJson = JSON.parse(data);
      let rows: Row[] = rowsJson.map((item: Row) => {
        item.x = Number(item.x);
        item.y = Number(item.y);
        item.label = Number(item.label);
        return item;
      });
      this.dataGrouped = this.utils.groupRowByLabel(rows);
      this.labels = this.utils.getLabels(rows);
    });
  }
}
