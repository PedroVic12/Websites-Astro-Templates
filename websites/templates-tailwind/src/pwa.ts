import { registerSW } from 'virtual:pwa-register';

registerSW({
    immediate: true,
    onRegistered(r) {
        console.log('PWA ativo: ', r);
    },

    onRegisterError(error) {
        console.error('Erro no PWA:', error);
    }
});
