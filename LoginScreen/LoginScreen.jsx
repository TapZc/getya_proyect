import styles from './LoginScreen.module.css';

const LoginScreen = () => {
    return (
      <div className={styles.container}>
        <img src="ruta-del-logo" alt="GetYa Logo" className={styles.logo} />
        <h2 className={styles.title}>Iniciar Sesión</h2>
        {/* Aquí pondremos el formulario después */}
      </div>
    );
  };
  
  export default LoginScreen;
  