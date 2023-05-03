import { InputText } from 'primereact/inputtext'
import { Controller, useForm } from 'react-hook-form'
import { Button } from 'primereact/button'
import { classNames } from 'primereact/utils'
import { Password } from 'primereact/password'
import { useState } from 'react'
import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { Calendar } from 'primereact/calendar';
import dayjs from "dayjs";
import { useLocation } from "react-router-dom";
import { useParams } from 'react-router-dom'

export const ConfirmAccount = () => {
    const defaultValues = { cui: '', nombres: '', apellidos: '', correo: '', contraseña: '', contraseña2: '', fecha_nac: '', numero_grupo: '', seccion: '' }
    //cui, nombres, apellidos, contraseña, correo, fecha de nacimiento, tipo, numero grupo, sección
    const navigate = useNavigate()
    const [loading, setLoading] = useState(false)
    const params = useParams();
    const idToken = params.id;

    const {
        control,
        formState: { errors },
        handleSubmit,
        reset
    } = useForm({ defaultValues })


    const getDatos = async () => {
        console.log('hola');
        console.log(idToken);
        verificarToken(idToken)
    };
    const verificarToken = async (idToken) => {
        console.log('llego');
        console.log(idToken);
        const response = await fetch(
            'http://146.190.198.15:5050' + "/user/verifyemail", {
            mode: 'cors',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': 'http://146.190.198.15:5050' + "/user/verifyemail",
            },
            'body': JSON.stringify(

                {
                    token: idToken
                }

            )
        }
        ).then((response) => response.json());
        console.log(response);
        return response;

    };


    useEffect(() => {
        getDatos();
    }, []);


    const getFormErrorMessage = (name) => {
        return errors[name]
            ? <small className='p-error'>{errors[name].message}</small>
            : <small className='p-error'>&nbsp;</small>
    }



    return (
        <>
            <div className='card w-11/12 md:w-2/5'>
                <div className='flex flex-col gap-3 p-fluid'>
                    <p className='text-4xl font-bold text-center'>Cuenta Confirmada </p>
                    <p className='text-2xl font-bold text-center'>Gracias por verificar su cuenta, ya puede iniciar sesión</p>
                    <Button
                        label='Iniciar sesión' className='p-button-outlined' severity='secondary'
                        onClick={() => navigate('/login')}
                        rounded
                    />
                </div>

            </div>
        </>
    )
}
