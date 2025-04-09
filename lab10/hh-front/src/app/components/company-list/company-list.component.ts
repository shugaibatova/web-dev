import { Component, OnInit } from '@angular/core';
import { Company } from '../../models/company';
import { CompanyService } from '../../services/company.service';
import { Vacancy } from '../../models/vacancy';


@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];
  vacancies: Vacancy[] = [];
  selectedCompanyId: number | null = null;

  constructor(private companyService: CompanyService) {}

  ngOnInit(): void {
    this.companyService.getCompanies().subscribe((data) => {
      this.companies = data;
    });
  }

  showVacancies(id: number) {
    this.selectedCompanyId = id;
    this.companyService.getCompanyVacancies(id).subscribe((data) => {
      this.vacancies = data;
    });
  }
}
