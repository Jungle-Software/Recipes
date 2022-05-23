import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import reportWebVitals from './reportWebVitals';

import Temp from './routes/Temp/Temp';
import Invoices from './routes/Temp/components/Invoices';

const root = ReactDOM.createRoot(document.getElementById('root')!);

root.render(
    <BrowserRouter>
        <Routes>
            {/* Let's be careful here, we may want to move to Switch routes based on changing requirements. */}
            <Route path='/' element={<Temp />}>
                <Route path='invoices' element={<Invoices />} />
                <Route 
                    path='*'
                    element={
                        <main style={{ padding: '1rem'}}>
                            <p>There's nothing here!</p>
                        </main>
                    }
                />
            </Route>
        </Routes>
    </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
