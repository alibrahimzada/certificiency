export class Role {
    id: string;
    roleName: string;
    permissions: { name: string, key: string; }[]
    notifications: { name: string, key: string; }[]

}