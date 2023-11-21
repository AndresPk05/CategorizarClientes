import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FileCsvService } from '../file-csv.service';
import { Client } from '../client';
import { GridClientsComponent } from '../grid-clients/grid-clients.component';
@Component({
  selector: 'app-clients-upload',
  standalone: true,
  imports: [CommonModule, GridClientsComponent],
  templateUrl: './clients-upload.component.html',
  styleUrl: './clients-upload.component.css'
})
export class ClientsUploadComponent {
  fileService : FileCsvService = inject(FileCsvService);
  clients: Client[] = [];
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
}
