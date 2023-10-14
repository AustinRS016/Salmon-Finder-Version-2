import { configureStore } from '@reduxjs/toolkit';
import hatcheryReducer from './hatcherySlice';
import filterReducer from './filterSlice';

export const store = configureStore({
	reducer: {
		hatchery: hatcheryReducer,
		filter: filterReducer,
	},
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
