import { InputText } from 'primereact/inputtext'
import { Controller, useForm } from 'react-hook-form'
import { Button } from 'primereact/button'
import { classNames } from 'primereact/utils'
import { Password } from 'primereact/password'
import { useState, useContext, } from 'react'
import { useNavigate } from 'react-router-dom'
import { Calendar } from 'primereact/calendar';
import dayjs from "dayjs";
import { Dropdown } from 'primereact/dropdown';
import { Context } from '../store/Context.jsx'
import DeleteUsuForm from './DeleteUsu.jsx';

export const AddUsuForm = () => {
    const defaultValues = { cui: '', nombres: '', apellidos: '', correo: '', contraseña: '', contraseña2: '', areaAsignada: '', fecha_nac: '', sueldo: '' }
    const { token, isAuth, getCountProducts } = useContext(Context)
    //cui, nombres, apellidos, contraseña, correo, fecha de nacimiento, tipo, numero grupo, sección
    const navigate = useNavigate()
    const [loading, setLoading] = useState(false)
    const tiposU = [
        { name: 'Empresario', code: 'E' },
        { name: 'Usuario Cliente', code: 'C' }
    ];
    const secc = [
        { name: 'N', code: 'N' },
        { name: 'A', code: 'A' }
    ];

    const {
        control,
        formState: { errors },
        handleSubmit,
        reset
    } = useForm({ defaultValues })

    const onSubmit = async (data) => {
        setLoading(true)
        let fech = data['fecha_nac']
        let for_date = formatDate(fech)
        data['fecha_nac'] = for_date

        console.log(data)
        const rest = await nuevoUsuario(data);
        setTimeout(() => {
            reset()
            setLoading(false)
        }, 2000)
        navigate('/AddUsu')
    }


    const nuevoUsuario = async (data) => {



        console.log('info ');
        console.log(data);
        const myFile = document.querySelector("input[type=file]");
        const dataform = new FormData();
        dataform.append("cui", data['cui']);
        dataform.append("nombres", data['nombres']);
        dataform.append("apellidos", data['apellidos']);
        dataform.append("password", data['contraseña']);
        dataform.append("confirmarPassword", data['contraseña2']);
        dataform.append("correo", data['correo']);
        dataform.append("fechaNacimiento", data['fecha_nac']);
        dataform.append("areaAsignada", data['areaAsignada']);
        dataform.append("sueldo", data['sueldo']);
        const response = await fetch('http://146.190.198.15:4009' + "/rrhh/agregarUsuario", {
            method: "POST",
            body: dataform,
            headers: {
                Authorization: `Bearer ${token}`
            }
        }).then((response) => response.json());
        console.log(response);
        return response;

        /*         const response = await fetch(
                    'http://146.190.198.15:4009' + "/rrhh/agregarUsuario", {
                    mode: 'cors',
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': 'http://146.190.198.15:4009' + "/rrhh/agregarUsuario",
                    },
                    'body': FormData.stringify(
                        {
                            cui: data['cui'],
                            nombres: data['nombres'],
                            apellidos: data['apellidos'],
                            password: data['contraseña'],
                            confirmarPassword: data['contraseña2'],
                            correo: data['correo'],
                            fecha_nacimiento: data['fecha_nac'],
                            areaAsignada: data['areaAsignada'],
                            sueldo: data['sueldo']
                        }
                    )
        
        
                    /*             JSON.stringify(
                                    {
                                        cui: data['cui'],
                                        nombres: data['nombres'],
                                        apellidos: data['apellidos'],
                                        contrasena: data['contraseña'],
                                        correo: data['correo'],
                                        fecha_nacimiento: data['fecha_nac'],
                                        tipo: "U"
                                    }
                                ) */
        /*         }
                ).then((response) => response.json());
                console.log(response);
                return response; */

    };

    const getFormErrorMessage = (name) => {
        return errors[name]
            ? <small className='p-error'>{errors[name].message}</small>
            : <small className='p-error'>&nbsp;</small>
    }

    const formatDate = (date) => {
        return dayjs(date).format("YYYY/MM/DD");
    };

    return (
        <>
            <div >

                <DeleteUsuForm></DeleteUsuForm>
            </div>
            <div className='card w-11/12 md:w-2/5'>

                <form onSubmit={handleSubmit(onSubmit)} className='flex flex-col gap-3 p-fluid'>
                    <p className='text-3xl font-bold text-center'>Agregar Usuario</p>

                    <Controller
                        name='cui'
                        control={control}
                        rules={{
                            required: 'cui es requerido.',
                            minLength: { value: 13, message: 'El CUI debe tener 13 dígitos' },
                            maxLength: { value: 13, message: 'El CUI debe tener 13 dígitos' },
                        }}
                        render={({ field, fieldState }) => (
                            <>
                                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                                <span className='p-float-label'>
                                    <InputText
                                        id={field.name} value={field.value}
                                        type="number"
                                        maxLength="13"
                                        pattern="[0-9]{0,13}"
                                        className={classNames({ 'p-invalid': fieldState.error })}
                                        onChange={(e) => field.onChange(e.target.value)}
                                    />
                                    <label htmlFor={field.name}>CUI *</label>
                                </span>
                                {getFormErrorMessage(field.name)}
                            </>
                        )}
                    />

                    <Controller
                        name='nombres'
                        control={control}
                        rules={{ required: 'nombres son requeridos.' }}
                        render={({ field, fieldState }) => (
                            <>
                                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                                <span className='p-float-label'>
                                    <InputText
                                        id={field.name} value={field.value}
                                        className={classNames({ 'p-invalid': fieldState.error })}
                                        onChange={(e) => field.onChange(e.target.value)}
                                    />
                                    <label htmlFor={field.name}>Nombres *</label>
                                </span>
                                {getFormErrorMessage(field.name)}
                            </>
                        )}
                    />

                    <Controller
                        name='apellidos'
                        control={control}
                        rules={{ required: 'apellidos son requeridos.' }}
                        render={({ field, fieldState }) => (
                            <>
                                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                                <span className='p-float-label'>
                                    <InputText
                                        id={field.name} value={field.value}
                                        className={classNames({ 'p-invalid': fieldState.error })}
                                        onChange={(e) => field.onChange(e.target.value)}
                                    />
                                    <label htmlFor={field.name}>Apellidos *</label>
                                </span>
                                {getFormErrorMessage(field.name)}
                            </>
                        )}
                    />

                    <Controller
                        name='correo'
                        control={control}
                        rules={{ required: 'correo es requerido.' }}
                        render={({ field, fieldState }) => (
                            <>
                                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                                <span className='p-float-label'>
                                    <InputText
                                        id={field.name} value={field.value} type='email'
                                        className={classNames({ 'p-invalid': fieldState.error })}
                                        onChange={(e) => field.onChange(e.target.value)}
                                    />
                                    <label htmlFor={field.name}>Correo *</label>
                                </span>
                                {getFormErrorMessage(field.name)}
                            </>
                        )}
                    />

                    <Controller
                        name='contraseña'
                        control={control}
                        rules={{
                            required: 'contraseña es requerido.',
                            minLength: { value: 5, message: 'La contraseña debe tener al menos 5 caracteres' }
                        }}
                        render={({ field, fieldState }) => (
                            <>
                                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                                <span className='p-float-label'>
                                    <Password
                                        id={field.name} value={field.value}
                                        className={classNames({ 'p-invalid': fieldState.error })}
                                        onChange={(e) => field.onChange(e.target.value)}
                                        feedback={false}
                                        toggleMask
                                    />
                                    <label htmlFor={field.name}>Contraseña *</label>
                                </span>
                                {getFormErrorMessage(field.name)}
                            </>
                        )}
                    />

                    <Controller
                        name='contraseña2'
                        control={control}
                        rules={{
                            required: 'contraseña es requerido.',
                            validate: (value, formValues) => value === formValues.contraseña || 'Contraseñas no coinciden'
                        }}
                        render={({ field, fieldState }) => (
                            <>
                                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                                <span className='p-float-label'>
                                    <Password
                                        id={field.name} value={field.value}
                                        className={classNames({ 'p-invalid': fieldState.error })}
                                        onChange={(e) => field.onChange(e.target.value)}
                                        feedback={false}
                                        toggleMask
                                    />
                                    <label htmlFor={field.name}>Confirmar Contraseña *</label>
                                </span>
                                {getFormErrorMessage(field.name)}
                            </>
                        )}
                    />

                    <Controller
                        name='fecha_nac'
                        control={control}
                        rules={{ required: 'Fecha es requerida.' }}
                        render={({ field, fieldState }) => (
                            <>
                                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                                <span className='p-float-label'>

                                    <Calendar
                                        id={field.name}
                                        name="date"
                                        dateFormat="dd/mm/yy"
                                        type={'month'}
                                        value={field.value}
                                        className={classNames({ 'p-invalid': fieldState.error })}
                                        onChange={(e) => field.onChange(e.target.value)}
                                    />
                                    <label htmlFor={field.name}>Fecha de Nacimiento *</label>
                                </span>
                                {getFormErrorMessage(field.name)}
                            </>
                        )}
                    />

                    <Controller
                        name='areaAsignada'
                        control={control}
                        rules={{
                            required: 'área asignada es requerido.'
                        }}
                        render={({ field, fieldState }) => (
                            <>
                                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                                <span className='p-float-label'>
                                    <InputText
                                        id={field.name} value={field.value}
                                        className={classNames({ 'p-invalid': fieldState.error })}
                                        onChange={(e) => field.onChange(e.target.value)}
                                    />
                                    <label htmlFor={field.name}>Área asignada *</label>
                                </span>
                                {getFormErrorMessage(field.name)}
                            </>
                        )}
                    />

                    <Controller
                        name="sueldo"
                        control={control}
                        rules={{ required: 'sueldo es requerido.' }}
                        render={({ field, fieldState }) => (
                            <>
                                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                                <span className='p-float-label'>
                                    <InputText
                                        id={field.name} value={field.value}
                                        type="number"
                                        pattern="[0-9]"
                                        className={classNames({ 'p-invalid': fieldState.error })}
                                        onChange={(e) => field.onChange(e.target.value)}
                                    />
                                    <label htmlFor={field.name}>Sueldo *</label>
                                </span>
                                {getFormErrorMessage(field.name)}
                            </>
                        )}
                    />


                    <Button label='Registrar usuario' loading={loading} rounded />
                    <Button
                        label='Cancelar' className='p-button-outlined' severity='secondary'
                        onClick={() => navigate('/shoppingCart')}
                        rounded
                    />
                </form>

            </div>
        </>
    )
}
