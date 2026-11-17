import { render, screen } from '@testing-library/react'
import { expect, test } from 'vitest'
import App from './App'

test('affiche le titre', () => {
    render(<App />)
    // Vérifie que le titre est bien affiché
    expect(screen.getByText('TP CI/CD de DevNest Academy')).toBeTruthy()
})