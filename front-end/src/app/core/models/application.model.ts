export class Application {
    application_id: string;
    event_id: string;
    user_id: string;
    applied_on: any;
    application_status: string;
}

export const APPLICATION_STATUS = [
    { text: 'Applied', code: 1},
    { text: 'Accepted', code: 2},
    { text: 'Rejected', code: 3},
    { text: 'Attended', code: 4},
    { text: 'Not Attended', code: 5},
    { text: 'Completed', code: 6}
]
