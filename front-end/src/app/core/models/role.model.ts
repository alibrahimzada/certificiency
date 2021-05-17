export class Role {
    role_id: string;
    role_name: string;
    role_permissions: { name: string, key: string; }[];
    customer_id: string;
}