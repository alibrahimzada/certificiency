
export class User {
    id: string
    firstName: string
    lastName: string
    username: string
    email: string
    identityNumber?: string
    phoneNumber?: string
    password: string
    address?: string
    companyId?: string
    roleId: string;
    engineerArea: {
        id: string;
        name: string;
        code: string;
    }[]
}
