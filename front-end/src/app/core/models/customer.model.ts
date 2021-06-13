import { Role } from "./role.model";
import { User } from "./user.model";

export class Customer{
    customer_id: string;
    customer_name: string;
    is_active: any;
    created_on: any;
    company_permissions: any;
    domain_name: string;
}

export class CustomerCreateModel {
    customer: Customer;
    role: Role;
    user: User;
}