import { InputText } from 'primereact/inputtext'
import { Controller, useForm } from 'react-hook-form'
import { Button } from 'primereact/button'
import { classNames } from 'primereact/utils'
import { Password } from 'primereact/password'
import { useState, useContext, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import { Calendar } from 'primereact/calendar';
import dayjs from "dayjs";
import { Dropdown } from 'primereact/dropdown';
import { Context } from '../store/Context.jsx'
import { Dialog } from 'primereact/dialog';
import { Toast } from 'primereact/toast';

export default function DeleteUsuForm() {
    const defaultValues = { cui: '' }
    const { token, isAuth, getCountProducts } = useContext(Context)
    //cui, nombres, apellidos, contraseña, correo, fecha de nacimiento, tipo, numero grupo, sección
    const navigate = useNavigate()
    const [loading, setLoading] = useState(false)
    const [visible, setVisible] = useState(false);
    const toast = useRef(null);

    const {
        control,
        formState: { errors },
        handleSubmit,
        reset
    } = useForm({ defaultValues })

    const onSubmit = async (data) => {
        setLoading(true)

        console.log(data)
        const rest = await deleteU(data);
        setTimeout(() => {
            reset()
            setLoading(false)
        }, 2000)
        navigate('/AddUsu')
    }


    const deleteU = async (data) => {



        console.log('info ');
        console.log(data);
        const dataform = new FormData();
        dataform.append("cui", data['cui']);
        const response = await fetch('http://146.190.198.15:4010' + "/rrhh/eliminarUsuarioAdmin", {
            method: "PUT",
            body: dataform,
            headers: {
                Authorization: `Bearer ${token}`
            }
        }).then((response) => response.json());
        console.log(response);
        toast.current.show({ severity: 'info', summary: 'Info', detail: response.mensaje });
        return response;


    };

    const getFormErrorMessage = (name) => {
        return errors[name]
            ? <small className='p-error'>{errors[name].message}</small>
            : <small className='p-error'>&nbsp;</small>
    }


    return (
        <>

            <Button label="Show" icon="pi pi-external-link" onClick={() => setVisible(true)} />
            <Dialog visible={visible} onHide={() => setVisible(false)}
                style={{ width: '50vw' }} breakpoints={{ '960px': '75vw', '641px': '100vw' }}>
                <form onSubmit={handleSubmit(onSubmit)} className='flex flex-col gap-3 p-fluid'>
                    <p className='text-3xl font-bold text-center'>Eliminar Usuario</p>

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





                    <Button label='Eliminar usuario' loading={loading} rounded />
                    <Button
                        label='Cancelar' className='p-button-outlined' severity='secondary'
                        onClick={() => navigate('/agregarUsuario')}
                        rounded
                    />
                </form>
            </Dialog>
            <Toast ref={toast} />
        </>
    )
}
