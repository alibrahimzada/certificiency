export class Application {
    application_id: string;
    event_id: string;
    user_id: string;
    applied_on: any;
    application_status: string;
}

export const APPLICATION_STATUS = [
    { text: 'Applied', code: 1},
    { text: 'Waiting List', code: 2},
    { text: 'Declined', code: 3},
    { text: 'Approved', code: 5},
    { text: 'Completed', code: 6}
]