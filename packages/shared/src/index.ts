export const FOOD_CATEGORIES = ["cooked_meals","bakery","fruits","vegetables","packaged","dairy"] as const;
export type FoodCategory = typeof FOOD_CATEGORIES[number];
export const DONATION_STATUSES = ["available","requested","approved","ready_for_pickup","picked_up","completed","expired"] as const;
export type DonationStatus = typeof DONATION_STATUSES[number];
export type MatchCandidate = {organizationId:string;name:string;verified:boolean;categories:FoodCategory[];capacityKg:number;maxDistanceKm?:number;storage:string[];location:[number,number]};
export type MatchInput = {location:[number,number];category:FoodCategory;quantityKg:number;deadline:string;storage:string[]};